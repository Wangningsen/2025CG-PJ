import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
w1=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().push([(3,-54)]).circle(46).push([(29,79)]).circle(21).finalize().extrude(-87).union(w0.workplane(offset=77/2).moveTo(-31,39).cylinder(77,14)).union(w1.workplane(offset=3/2).moveTo(26.5,-10.5).box(19,79,3))