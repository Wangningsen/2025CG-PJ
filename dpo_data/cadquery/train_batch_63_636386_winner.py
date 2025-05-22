import cadquery as cq
w0=cq.Workplane('YZ',origin=(50,0,0))
r=w0.sketch().arc((-2,62),(-65,-83),(64,5)).segment((83,20)).segment((82,22)).segment((97,34)).segment((83,51)).segment((82,64)).segment((70,64)).segment((38,100)).close().assemble().finalize().extrude(-99)