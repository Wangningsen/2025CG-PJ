import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
w1=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().segment((-74,-16),(-74,56)).arc((-100,20),(-74,-16)).assemble().reset().face(w0.sketch().arc((-51,-16),(-25,20),(-51,56)).close().assemble()).push([(-6.5,-83)]).rect(43,28).push([(46.5,95)]).rect(107,4).finalize().extrude(-100).union(w0.sketch().push([(-57,82.5)]).rect(30,15).push([(-70,88)]).circle(1,mode='s').finalize().extrude(65)).union(w1.sketch().segment((12,-40),(57,-40)).segment((57,-95)).arc((69,-39),(12,-40)).assemble().finalize().extrude(-47))