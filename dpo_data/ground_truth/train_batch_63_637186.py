import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('ZX',origin=(0,19,0))
r=w0.sketch().arc((42,-8),(73,2),(81,33)).arc((62,28),(43,30)).arc((46,11),(42,-8)).assemble().finalize().extrude(-116).union(w0.sketch().arc((-48,6),(-91,-56),(-17,-41)).arc((4,-30),(12,-9)).arc((93,47),(0,16)).arc((-26,22),(-48,6)).assemble().push([(48.5,25)]).rect(53,64,mode='s').finalize().extrude(84)).union(w1.sketch().arc((14,66),(15,19),(49,51)).arc((51,60),(48,69)).segment((48,38)).segment((31,38)).segment((31,79)).arc((20,75),(14,66)).assemble().finalize().extrude(27))