# Segmentation

- Segments are a logical unit such as
    - main program
    - function, object


## Segmentation table

- Logical address (seg#, offset)
    - Offset has the same length as physical address

- **Segmentation table**, each entry has
    - Base : start of physical address
    - Limit : the length of the segment

- Segment-table bse register (STBR): the physical address of the segmentation table
- Segement-table length register (STLR): the number of segments

### Segmentation hardware

- Limit register is used to check offset length
- MMU allocate memory by assigning an appropriate base address for each segment



## Protection and Sharing

- Protection bits associated with segments
    - Readonly segment (code)
    - Read-write segments (data,heap,stack)

- Code sharing occurs at **segment level** 
    - **Shared memory communication** 
    - **Shared library**





## Segmentation with Paging

- Apply **segmentation** in logical address space 
- Apply **paging** in physical address space

### Address Translation

- CPU generates logical address



