A wrapper for [WhiteStripe](https://github.com/muschellij2/WhiteStripe). For example,

```py
import WhiteStripe as ws
t1 = ws.readnii("T1w.nii.gz")
ind = ws.whitestripe(t1, "T1")
ind = ind[ind.names.index('whitestripe.ind')]

res = ws.whitestripe_norm(t1, ind)
ws.writenii(res, "T1w_ws.nii.gz")
```