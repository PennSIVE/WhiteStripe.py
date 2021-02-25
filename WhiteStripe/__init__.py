from rpy2.robjects.packages import importr

neurobase = importr("neurobase")
WhiteStripe = importr("WhiteStripe")


def readnii(file):
    return neurobase.readnii(file);


def writenii(data, file):
    return neurobase.writenii(data, file);


def whitestripe(image, ws_type):
    return Whitestripe.whitestripe(image, ws_type); 


def whitestripe_norm(image, ind):
    return Whitestripe.whitestripe_norm(image, ind); 
