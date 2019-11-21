# File Objects
with open('comicCover.jpg', 'rb') as rf:
    with open('comicCover_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
    
    
    

    