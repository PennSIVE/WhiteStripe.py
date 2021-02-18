from rpy2.robjects import r
from rpy2.robjects.packages import importr

importr("neurobase")
importr("WhiteStripe")


def read(file):
    return r("readnii('%s')" % (file))


def write(data, file):
    r.assign('data', data)
    return r("writenii(data, '%s')" % (file))


def whitestripe(image, ws_type):
    r.assign('image', image)
    res = r("whitestripe(image, \"%s\")" % (ws_type))
    return {
    	'whitestripe.ind': res[0],
    	'img.mode': res[1],
    	'mask.img': res[2],
    	'mu.whitestripe': res[3],
    	'sig.whitestripe': res[4],
    	'img.mode.q': res[5],
    	'whitestripe': res[6],
    	'whitestripe.width': res[7],
    	'whitestripe.width.l': res[8],
    	'whitestripe.width.u': res[9],
    	'err': res[10],
    }


def whitestripe_norm(image, ind):
    r.assign('ind', ind)
    r.assign('image', image)
    return r("whitestripe_norm(image, ind)")
