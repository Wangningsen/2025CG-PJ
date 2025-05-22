import cadquery as cq
w0=cq.Workplane('YZ',origin=(98,0,0))
r=w0.sketch().segment((-97,-24),(-97,-9)).segment((12,-9)).segment((12,-76)).segment((-65,-76)).arc((56,-83),(95,31)).segment((94,31)).segment((94,33)).arc((-29,96),(-97,-24)).assemble().finalize().extrude(-196)