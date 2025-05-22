import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-72))
r=w0.sketch().segment((86,-28),(100,-28)).segment((100,-18)).arc((94,-23),(86,-25)).close().assemble().finalize().extrude(15).union(w0.sketch().arc((-73,41),(-50,-52),(-23,37)).arc((-45,98),(-73,41)).assemble().push([(-71,-22)]).circle(20,mode='s').push([(-8,-80)]).circle(18).finalize().extrude(144))