import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-32,0))
w1=cq.Workplane('ZX',origin=(0,-9,0))
r=w0.sketch().segment((-2,-43),(24,-43)).segment((24,-11)).arc((49,-10),(70,5)).arc((55,16),(75,13)).arc((85,29),(100,37)).arc((32,79),(1,-4)).segment((-2,-4)).close().assemble().finalize().extrude(-6).union(w1.sketch().segment((-100,-83),(-9,-83)).segment((-9,-38)).arc((35,-34),(33,10)).arc((26,51),(10,14)).arc((-18,1),(-16,-30)).segment((-16,-33)).segment((-100,-33)).close().assemble().finalize().extrude(47))