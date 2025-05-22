import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,76))
r=w0.sketch().push([(0,-28.5)]).rect(192,143).push([(0,-28)]).circle(66,mode='s').finalize().extrude(-153).union(w0.sketch().segment((-23,90),(82,91)).segment((81,100)).segment((-23,99)).close().assemble().finalize().extrude(-146))