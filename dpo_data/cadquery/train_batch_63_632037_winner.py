import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
r=w0.sketch().segment((-27,-26),(-24,-26)).segment((-24,-49)).segment((-13,-49)).segment((-6,-26)).segment((83,-26)).segment((83,100)).segment((-27,100)).close().assemble().finalize().extrude(-48).union(w0.sketch().push([(-64.5,-57)]).rect(37,86).push([(-49,-55)]).circle(2,mode='s').finalize().extrude(-26))