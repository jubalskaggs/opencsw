PHP5EXT_NAME = xsl

define CSWphp5xsl_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling xsl extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "xsl"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=xsl.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=xsl.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=xsl.so|extension=xsl.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=xsl.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "xsl"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5xsl_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling xsl extension"

perl -i -plne 's|extension=xsl.so|;extension=xsl.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "xsl"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef
