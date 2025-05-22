import cadquery as cq
w0=cq.Workplane('YZ',origin=(-27,0,0))
w1=cq.Workplane('ZX',origin=(0,-13,0))
r=w0.sketch().arc((-42,50),(-89,-25),(-8,6)).arc((0,5),(8,6)).segment((16,6)).segment((16,-53)).segment((100,-53)).segment((100,32)).segment((68,32)).arc((66,48),(57,61)).segment((57,94)).segment((-42,94)).close().assemble().reset().face(w0.sketch().arc((-37,45),(-22,39),(-10,27)).arc((-15,46),(-37,45)).assemble(),mode='s').finalize().extrude(56).union(w1.sketch().push([(-65,0)]).circle(29).push([(-67.5,-26.5)]).rect(3,5,mode='s').finalize().extrude(-33))