import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().push([(-49,-10)]).circle(51).circle(43,mode='s').reset().face(w0.sketch().segment((90,-22),(100,-22)).segment((100,11)).segment((97,11)).arc((-5,28),(90,-22)).assemble()).finalize().extrude(-55)