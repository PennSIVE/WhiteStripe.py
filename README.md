A wrapper for [WhiteStripe](https://github.com/muschellij2/WhiteStripe). For example,

```py
import WhiteStripe as ws
t1 = ws.read("T1w.nii.gz")
ind = ws.whitestripe(t1, "T1")['whitestripe.ind']
res = ws.whitestripe_norm(t1, ind)
ws.write(res, "T1w_ws.nii.gz")
```