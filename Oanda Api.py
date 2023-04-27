#!/usr/bin/env python
# coding: utf-8

# # First Steps with the OANDA API

# ## Connecting to the API / Server

# In[25]:


import pandas as pd
import tpqoa


# In[26]:


api = tpqoa.tpqoa("oanda.cfg")


# In[27]:


api.get_history("EUR_USD","2020-3-12","2020-3-13","M1","A")


# In[29]:


api.get_account_summary()


# In[30]:


api.account_type


# In[31]:


api.account_id


# In[32]:


api.get_instruments()


# In[34]:


instr = api.get_instruments()


# In[35]:


len(instr)


# ## Getting Historical Data (Part 1)

# In[10]:


import pandas as pd
import tpqoa


# In[13]:


api.get_history(instrument = "EUR_USD", start = "2020-07-01", end = "2020-07-31",
                granularity = "D", price = "B")


# In[38]:


api = tpqoa.tpqoa("oanda.cfg")


# In[39]:


df = api.get_history(instrument = "EUR_USD", start = "2020-07-01", end = "2020-07-31",
                granularity = "D", price = "B")


# In[40]:


df.info()


# In[41]:


api.get_history(instrument = "EUR_USD", start = "2020-07-01", end = "2020-07-01",
                granularity = "D", price = "A")


# ## Getting Historical Data (Part 2)

# In[42]:


api.get_history("EUR_USD", "2020-08-03", "2020-08-05", "H1", "A")


# In[43]:


api.get_history("EUR_USD", "2020-08-03", "2020-08-05", "H12", "A")


# In[44]:


api.get_history("EUR_USD", "2020-08-03", "2020-08-05", "M1", "A")


# In[21]:


api.get_history("EUR_USD", "2020-08-03", "2020-08-04", "S5", "A")


# In[23]:


api.get_history("SPX500_USD", "2020-08-03", "2020-08-04", "H1", "A")


# ## Streaming high-frequency real-time Data

# In[45]:


import pandas as pd
import tpqoa


# In[46]:


api = tpqoa.tpqoa("oanda.cfg")


# In[ ]:


api.stream_data('EUR_USD') 


# In[ ]:


api.stop_stream()


# In[ ]:





# ## Creating Orders and Executing Trades

# In[ ]:


import pandas as pd
import tpqoa


# In[ ]:


api = tpqoa.tpqoa("oanda.cfg")


# In[ ]:


api.create_order(instrument = "EUR_USD", units = 100000, sl_distance= 0.1)


# In[ ]:


api.create_order(instrument = "EUR_USD", units = -100000, sl_distance= 0.1)


# In[ ]:


api.get_account_summary()


# In[ ]:


api.get_transactions(tid = 24)


# In[ ]:


api.print_transactions(tid = 26-1)


# In[ ]:




