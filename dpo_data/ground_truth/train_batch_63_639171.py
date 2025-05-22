import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
w1=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().push([(47,-35)]).rect(14,62).rect(6,12,mode='s').finalize().extrude(-42).union(w0.sketch().push([(32,6)]).circle(57).push([(32.5,5.5)]).rect(87,5,mode='s').finalize().extrude(57)).union(w1.sketch().segment((-26,-89),(100,-89)).segment((100,-44)).segment((39,-44)).segment((39,-10)).segment((27,-10)).segment((27,-44)).segment((-26,-44)).close().assemble().push([(37.5,-66)]).rect(3,40,mode='s').finalize().extrude(39))