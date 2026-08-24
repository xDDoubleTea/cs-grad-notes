#!/usr/bin/env python3
"""
Linear algebra practice generator.

Core idea: build matrices BACKWARD from a known clean answer, using integer
elementary row operations (which have determinant +-1). This guarantees
integer inverses / prescribed eigenvalues / prescribed Jordan form, so you
never waste drill time fighting fractions instead of practicing the method.

Usage:
    python3 la_practice_gen.py inverse   [--n 4]
    python3 la_practice_gen.py diag      [--n 4] [--eig 1,1,2,4]
    python3 la_practice_gen.py jordan    [--blocks 3:2,3:1,5:1]   (eig:size,...)

Answers are hidden by default; pass --reveal to print them immediately
(useful for building an answer key file instead of self-testing).
"""

import argparse
import random
import sympy


def random_unimodular(n, steps=6, coeff_range=2, seed=None):
    """Integer matrix with det = +-1, built from I via random elementary
    row operations (row swap, or row_i += c * row_j)."""
    if seed is not None:
        random.seed(seed)
    M = sympy.eye(n)
    for _ in range(steps):
        if n > 1 and random.random() < 0.15:
            i, j = random.sample(range(n), 2)
            M.row_swap(i, j)
        else:
            i, j = random.sample(range(n), 2)
            c = random.choice(
                [x for x in range(-coeff_range, coeff_range + 1) if x != 0]
            )
            M[i, :] = M[i, :] + c * M[j, :]
    return M


def gen_inverse_practice(n, steps):
    A = random_unimodular(n, steps)
    return A, {"A_inverse": A.inv()}


def gen_diag_practice(n, eigenvalues, steps):
    assert len(eigenvalues) == n, "need exactly n eigenvalues"
    P = random_unimodular(n, steps)
    D = sympy.diag(*eigenvalues)
    A = P * D * P.inv()
    A = A.applyfunc(sympy.nsimplify)
    return A, {"eigenvalues": eigenvalues, "D": D, "P_used": P}


def gen_jordan_practice(blocks, steps):
    """blocks: list of (eigenvalue, size) tuples."""
    n = sum(size for _, size in blocks)
    J = sympy.zeros(n, n)
    pos = 0
    for val, size in blocks:
        for i in range(size):
            J[pos + i, pos + i] = val
            if i > 0:
                J[pos + i - 1, pos + i] = 1
        pos += size
    P = random_unimodular(n, steps)
    A = P * J * P.inv()
    A = A.applyfunc(sympy.nsimplify)
    return A, {"jordan_blocks": blocks, "J": J, "P_used": P}


def parse_eig(s):
    return [int(x) for x in s.split(",")]


def parse_blocks(s):
    out = []
    for part in s.split(","):
        val, size = part.split(":")
        out.append((int(val), int(size)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["inverse", "diag", "jordan"])
    ap.add_argument("--n", type=int, default=4)
    ap.add_argument(
        "--eig",
        type=str,
        default=None,
        help="comma-separated eigenvalues, e.g. 1,1,2,4",
    )
    ap.add_argument(
        "--blocks",
        type=str,
        default=None,
        help="comma-separated eig:size pairs, e.g. 3:2,3:1,5:1",
    )
    ap.add_argument(
        "--steps",
        type=int,
        default=6,
        help="number of random elementary ops used to build P "
        "(keep this small, e.g. 4-8, or entries blow up)",
    )
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument(
        "--reveal",
        action="store_true",
        help="print the answer immediately instead of hiding it",
    )
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.mode == "inverse":
        A, answer = gen_inverse_practice(args.n, args.steps)
        print("=== Find A^-1 by Gauss-Jordan ===")
        sympy.pprint(A)
        if args.reveal:
            print("\n--- answer ---")
            sympy.pprint(answer["A_inverse"])
        else:
            print("\n(run again with --reveal to check your answer)")

    elif args.mode == "diag":
        eig = (
            parse_eig(args.eig)
            if args.eig
            else [random.randint(-4, 4) for _ in range(args.n)]
        )
        A, answer = gen_diag_practice(args.n, eig, args.steps)
        print("=== Diagonalize A (find eigenvalues + eigenvectors) ===")
        sympy.pprint(A)
        if args.reveal:
            print("\n--- answer: eigenvalues ---")
            print(answer["eigenvalues"])
            print("--- D ---")
            sympy.pprint(answer["D"])
        else:
            print("\n(run again with --reveal to check your answer)")

    elif args.mode == "jordan":
        blocks = parse_blocks(args.blocks) if args.blocks else [(2, 2), (2, 1), (5, 1)]
        A, answer = gen_jordan_practice(blocks, args.steps)
        print("=== Find the Jordan normal form of A ===")
        sympy.pprint(A)
        if args.reveal:
            print("\n--- answer: J ---")
            sympy.pprint(answer["J"])
        else:
            print("\n(run again with --reveal to check your answer)")


if __name__ == "__main__":
    main()
