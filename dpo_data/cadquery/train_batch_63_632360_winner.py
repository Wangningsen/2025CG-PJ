import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
r=w0.sketch().segment((-58,-100),(26,-100)).segment((26,-73)).arc((52,-40),(41,0)).segment((42,0)).segment((42,15)).arc((9,100),(-17,13)).segment((-17,9)).arc((-28,6),(-38,-1)).segment((-58,-1)).close().assemble().finalize().extrude(-46)