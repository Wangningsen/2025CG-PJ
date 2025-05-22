import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
r=w0.sketch().segment((-58,-28),(-56,-35)).arc((-53,-63),(-38,-86)).segment((-35,-93)).segment((-31,-91)).arc((-21,-98),(-12,-100)).segment((-12,-34)).segment((58,-34)).arc((50,-14),(35,3)).segment((33,8)).segment((30,6)).arc((-20,9),(-54,-27)).close().assemble().push([(37,79)]).circle(21).finalize().extrude(-24)