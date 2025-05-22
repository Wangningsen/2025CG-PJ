import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-48,-12),(-38,-24)).segment((-38,-73)).segment((38,-73)).segment((38,5)).segment((48,12)).segment((38,24)).segment((38,73)).segment((-38,73)).segment((-38,-5)).close().assemble().push([(-6,40)]).circle(13,mode='s').finalize().extrude(-200)