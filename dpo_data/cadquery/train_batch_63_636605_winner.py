import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
w1=cq.Workplane('XY',origin=(0,0,-58))
r=w0.sketch().segment((-94,3),(-56,3)).segment((-56,2)).segment((-43,-9)).segment((-14,-37)).segment((-14,-80)).segment((11,-80)).segment((11,-61)).segment((27,-77)).segment((66,-39)).segment((11,14)).segment((11,56)).segment((-14,56)).segment((-14,38)).segment((-30,56)).segment((-57,28)).segment((-57,75)).segment((-94,75)).close().assemble().push([(35,78)]).circle(22).finalize().extrude(124).union(w1.workplane(offset=-6/2).moveTo(28,-34).cylinder(6,66))