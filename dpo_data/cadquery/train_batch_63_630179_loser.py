import cadquery as cq
w0=cq.Workplane('YZ',origin=(-26,0,0))
w1=cq.Workplane('XY',origin=(0,0,-44))
r=w0.sketch().segment((78,-100),(86,-100)).segment((86,-73)).arc((91,-63),(86,-51)).segment((86,-26)).segment((78,-26)).segment((78,-51)).arc((74,-63),(78,-73)).close().assemble().finalize().extrude(-64).union(w0.workplane(offset=115/2).moveTo(15,-41).cylinder(115,28)).union(w1.sketch().arc((-44,-54),(-55,-84),(-23,-80)).arc((-23,-61),(-44,-54)).assemble().finalize().extrude(144))