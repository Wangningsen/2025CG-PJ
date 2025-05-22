import cadquery as cq
w0=cq.Workplane('YZ',origin=(50,0,0))
r=w0.sketch().arc((-5,63),(-66,-82),(63,5)).segment((96,36)).segment((37,100)).close().assemble().finalize().extrude(-99)