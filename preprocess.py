#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, glob, shutil
from midi2img import midi2image


# In[8]:


dataset_path = f"C:\midi\maestro-v2.0.0-midi\maestro-v2.0.0"
output_path = f"C:\midi\data"


# In[9]:


files = glob.glob(os.path.join(dataset_path,"*\*.midi"))
print(f"{len(files)} midi files were found")
for i,fp in enumerate(files):
    
    curdir = os.path.join(output_path, str(i))
    if not os.path.exists(curdir):
        os.mkdir(curdir)
    shutil.copy2(fp,curdir)
    midi2image(fp, curdir, 200)
    print(f"Done {i}/{len(files)}")
print("Finished")

# In[ ]:




