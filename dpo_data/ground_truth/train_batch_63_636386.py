import cadquery as cq
w0=cq.Workplane('YZ',origin=(50,0,0))
r=w0.sketch().arc((-9,63),(-66,-82),(63,5)).segment((75,17)).segment((82,17)).segment((82,23)).segment((96,35)).segment((82,51)).segment((82,64)).segment((71,64)).segment((37,100)).segment((-2,64)).segment((-9,64)).close().assemble().finalize().extrude(-99)