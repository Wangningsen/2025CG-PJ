import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,29))
r=w0.workplane(offset=-104/2).moveTo(-38,-30).box(82,36,104).union(w0.sketch().segment((-73,85),(-46,27)).segment((-37,32)).segment((-37,18)).segment((12,18)).segment((12,88)).segment((-34,88)).segment((-41,100)).close().assemble().push([(-15,54)]).circle(7,mode='s').push([(26.5,-99.5)]).rect(105,1).finalize().extrude(46))