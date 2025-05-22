import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
w1=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().segment((-96,84),(-79,81)).segment((-79,72)).segment((-26,72)).segment((-8,69)).segment((-6,86)).segment((-22,88)).segment((-22,97)).segment((-76,97)).segment((-93,100)).close().assemble().push([(42,-55)]).circle(29).finalize().extrude(-67).union(w0.workplane(offset=-3/2).moveTo(84,32.5).box(24,59,3)).union(w1.sketch().push([(-54,-23)]).rect(92,28).circle(11,mode='s').finalize().extrude(47))