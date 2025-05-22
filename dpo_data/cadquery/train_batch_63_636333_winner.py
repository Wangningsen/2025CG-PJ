import cadquery as cq
w0=cq.Workplane('YZ',origin=(98,0,0))
r=w0.sketch().arc((-97,-24),(89,45),(-65,-76)).segment((12,-76)).segment((12,-9)).segment((-97,-9)).close().assemble().finalize().extrude(-196)