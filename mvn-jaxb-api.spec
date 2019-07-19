#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jaxb-api
Version  : 2.2.2
Release  : 2
URL      : https://repo1.maven.org/maven2/javax/xml/bind/jaxb-api/2.2.2/jaxb-api-2.2.2.jar
Source0  : https://repo1.maven.org/maven2/javax/xml/bind/jaxb-api/2.2.2/jaxb-api-2.2.2.jar
Source1  : https://repo1.maven.org/maven2/javax/xml/bind/jaxb-api/2.2.11/jaxb-api-2.2.11.jar
Source2  : https://repo1.maven.org/maven2/javax/xml/bind/jaxb-api/2.2.11/jaxb-api-2.2.11.pom
Source3  : https://repo1.maven.org/maven2/javax/xml/bind/jaxb-api/2.2.2/jaxb-api-2.2.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.1 GPL-2.0-only
Requires: mvn-jaxb-api-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jaxb-api package.
Group: Data

%description data
data components for the mvn-jaxb-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.2/jaxb-api-2.2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.11
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.11/jaxb-api-2.2.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.11/jaxb-api-2.2.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.2/jaxb-api-2.2.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.11/jaxb-api-2.2.11.jar
/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.11/jaxb-api-2.2.11.pom
/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.2/jaxb-api-2.2.2.jar
/usr/share/java/.m2/repository/javax/xml/bind/jaxb-api/2.2.2/jaxb-api-2.2.2.pom
