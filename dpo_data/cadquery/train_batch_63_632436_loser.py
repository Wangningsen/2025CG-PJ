import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('ZX',origin=(0,34,0))
r=w0.sketch().push([(-47,39)]).circle(53).push([(-42,-27)]).circle(7).push([(-43,-27)]).circle(3,mode='s').finalize().extrude(-18).union(w0.sketch().segment((-19,-58),(-8,-73)).segment((5,-63)).arc((10,-64),(14,-65)).arc((35,-93),(65,-75)).segment((87,-82)).segment((100,-27)).segment((89,-24)).arc((69,3),(37,0)).segment((1,8)).close().assemble().finalize().extrude(-9)).union(w1.sketch().push([(-38,-1)]).circle(15).push([(-36.5,6.5)]).rect(5,5,mode='s').finalize().extrude(-85))