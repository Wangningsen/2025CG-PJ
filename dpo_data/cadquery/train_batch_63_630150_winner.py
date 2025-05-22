import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-27,-55),(31,-55)).segment((67,-76)).segment((100,-20)).segment((28,20)).segment((28,36)).segment((8,36)).arc((-93,48),(-27,-31)).close().assemble().finalize().extrude(-43)