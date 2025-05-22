import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-39,0))
w1=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().segment((31,-100),(31,-95)).segment((33,-95)).segment((33,-40)).segment((83,-40)).arc((-30,13),(31,-100)).assemble().finalize().extrude(86).union(w1.sketch().segment((-84,-4),(-21,-4)).segment((-21,-55)).segment((67,-55)).segment((67,-20)).segment((17,-20)).segment((17,100)).segment((-84,100)).close().assemble().finalize().extrude(-9))