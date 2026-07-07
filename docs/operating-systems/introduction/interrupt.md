# Interrupt

> Modern OS are interrupt (event) driven

- Interrupt is disabled when OS is currently processing interrupt
- Need to save the interrupted program's state

## Example

- The mouse recieves a left click signal
- The mouse send a interrupt signal to cpu
- CPU recieves interrupt, transfers control to interrupt handler
- OS calls the program that handles mouse clicks
- CPU resumes the interrupted task

## HW interrupt

- Also called **signal**


## SW interrupt

- Also called **trap**
- **Error**
- **System call**
