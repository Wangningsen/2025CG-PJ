import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
w1=cq.Workplane('ZX',origin=(0,53,0))
r=w0.workplane(offset=29/2).moveTo(-65,-26).box(70,84,29).union(w1.workplane(offset=47/2).moveTo(41,-12).box(54,36,47))