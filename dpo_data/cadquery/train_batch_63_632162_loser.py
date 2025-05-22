import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
w1=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().push([(-20,3.5)]).rect(38,137).push([(-20,4)]).circle(2,mode='s').finalize().extrude(-126).union(w0.sketch().arc((-14,-100),(-10,-82),(0,-65)).segment((-14,-65)).segment((-14,-50)).segment((46,-50)).arc((-14,-15),(-14,-84)).close().assemble().finalize().extrude(-44)).union(w1.sketch().segment((-46,-18),(25,-18)).segment((25,100)).segment((-46,100)).segment((-46,98)).segment((-33,98)).segment((-33,18)).segment((-46,18)).close().assemble().finalize().extrude(62))