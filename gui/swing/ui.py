from javax.swing import UIManager
from javax.swing import SwingUtilities


LAF="com.sun.java.swing.plaf.motif.MotifLookAndFeel"
#LAF="javax.swing.plaf.metal.MetalLookAndFeel"
#LAF="javax.swing.plaf.nimbus.NimbusLookAndFeel"
#LAF="com.sun.java.swing.plaf.gtk.GTKLookAndFeel"


UIManager.setLookAndFeel(LAF)
SwingUtilities.updateComponentTreeUI(frame)