import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
w1=cq.Workplane('XY',origin=(0,0,27))
r=w0.workplane(offset=-42/2).moveTo(47,-35).box(14,62,42).union(w0.sketch().push([(32,6)]).circle(57).push([(32.5,5.5)]).rect(87,5,mode='s').finalize().extrude(57)).union(w1.sketch().segment((-26,-89),(100,-89)).segment((100,-44)).segment((39,-44)).segment((39,-11)).segment((27,-11)).segment((27,-44)).segment((-26,-44)).close().assemble().push([(37.5,-64.5)]).rect(3,27,mode='s').finalize().extrude(39))