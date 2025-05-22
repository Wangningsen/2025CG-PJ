import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-48,-11),(-43,-23)).segment((-38,-21)).segment((-38,-73)).segment((38,-73)).segment((38,7)).segment((48,11)).segment((43,23)).segment((38,21)).segment((38,73)).segment((-38,73)).segment((-38,-7)).close().assemble().push([(-6,40)]).circle(13,mode='s').finalize().extrude(-200)