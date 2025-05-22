import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,18,0))
w1=cq.Workplane('YZ',origin=(-56,0,0))
r=w0.sketch().segment((-74,-16),(-74,56)).arc((-100,20),(-74,-16)).assemble().reset().face(w0.sketch().arc((-51,-16),(-25,20),(-51,56)).close().assemble()).push([(-6.5,-83)]).rect(43,28).push([(46.5,95)]).rect(107,4).finalize().extrude(-101).union(w0.workplane(offset=64/2).moveTo(-57,82.5).box(30,15,64)).union(w1.sketch().segment((13,-40),(57,-40)).segment((57,-95)).arc((69,-38),(13,-40)).assemble().finalize().extrude(47))