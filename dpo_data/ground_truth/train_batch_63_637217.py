import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().arc((58,-7),(79,2),(79,26)).arc((72,7),(58,-7)).assemble().finalize().extrude(-20).union(w0.sketch().push([(76,42)]).circle(24).circle(6,mode='s').finalize().extrude(-8)).union(w0.sketch().segment((-100,-62),(-21,-62)).arc((45,3),(-47,-3)).segment((-100,-3)).close().assemble().finalize().extrude(78))