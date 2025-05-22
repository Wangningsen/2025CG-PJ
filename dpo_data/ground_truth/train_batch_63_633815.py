import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
w1=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().push([(40,74)]).circle(26).circle(15,mode='s').finalize().extrude(-81).union(w0.sketch().arc((-36,31),(-62,-29),(1,-46)).arc((6,-25),(20,-9)).arc((13,14),(-5,29)).segment((-7,22)).close().assemble().finalize().extrude(6)).union(w1.sketch().segment((-100,12),(-48,12)).segment((-48,-18)).segment((16,-18)).arc((32,-35),(53,-28)).arc((51,-14),(57,-27)).arc((86,47),(9,25)).segment((-48,25)).segment((-48,16)).segment((-100,16)).close().assemble().finalize().extrude(-17))