# $Id$

import unittest
import sys
sys.path.append("../lib/python")
import gartest

class ExampleEndToEndTest(unittest.TestCase):
  """An example end-to-end test of GAR."""

  def testPkginfoName(self):
    """Checks that the GARNAME makes it to the NAME in pkginfo."""
    mybuild = gartest.DynamicGarBuild()
    mybuild.SetGarVariable("GARNAME", "foo")
    mybuild.AddInstallFile("/opt/csw/share/foo", "bar!\n")
    mybuild.WriteGarFiles()
    self.assertEquals(0, mybuild.Build())
    pkg = mybuild.GetFirstBuiltPackage()
    pkginfo = pkg.GetParsedPkginfo()
    # By default, the garname should be used to create the catalog name, which
    # in turn ends up in the NAME field in pkginfo.
    self.assertTrue(pkginfo["NAME"].startswith("foo"))


class StaticBuildTestExample(unittest.TestCase):
  """An example of a static build.

  This uses a static directory where GAR can be called.
  """

  def testLooseFiles(self):
    mybuild = gartest.StaticGarBuild("static/example")
    mybuild.Build()
    pkg = mybuild.GetFirstBuiltPackage()
    pkginfo = pkg.GetParsedPkginfo()
    # This part would often use "self.assertEqual(<expected>, <actual>)"
    self.assertTrue(pkginfo["NAME"].startswith("loose"))

# To add more tests, create a Python file similar to this one, and add the
# corresponding import statement to the run_tests.py file.
