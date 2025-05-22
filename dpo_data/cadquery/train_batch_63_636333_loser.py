import cadquery as cq
w0=cq.Workplane('YZ',origin=(98,0,0))
r=w0.sketch().segment((-97,-24),(-97,-9)).segment((12,-9)).segment((12,-76)).segment((-65,-76)).arc((84,54),(-97,-24)).assemble().finalize().extrude(-196)