import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().push([(-4,-1)]).rect(52,60).rect(50,24,mode='s').finalize().extrude(-75).union(w0.sketch().segment((12,-57),(14,-58)).segment((16,-56)).arc((-22,54),(12,-57)).assemble().finalize().extrude(125))