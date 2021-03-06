from conans import ConanFile, CMake

class AppConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "OpenSSL/1.0.2m@conan/stable", \
        "boost/1.66.0@conan/stable", \
        "cpprestsdk/2.10.1@bincrafters/stable", \
        "fmt/5.1.0@bincrafters/stable", \
        "gtest/1.8.0@bincrafters/stable", \
        "cryptopp/5.6.5@bincrafters/stable", \
        "Poco/1.8.1@pocoproject/stable", \
        "sqlpp11-connector-postgresql/0.2@vkrapivin/testing", \
        "aws-sdk-cpp/1.4.23@smela/testing", \
        "stb/20180214@conan/stable", \
        "jsonformoderncpp/3.1.2@vthiery/stable", \
        "libharu/[>=2.3.0]@joakimono/stable"
    default_options = "OpenSSL:shared=False", \
        "boost:shared=False", \
        "cpprestsdk:shared=False", \
        "gtest:shared=False", \
        "Poco:shared=False", \
        "Poco:enable_xml=True", \
        "Poco:enable_json=False", \
        "Poco:enable_mongodb=False", \
        "Poco:enable_pdf=False", \
        "Poco:enable_util=True", \
        "Poco:enable_net=True", \
        "Poco:enable_netssl=True", \
        "Poco:enable_netssl_win=True", \
        "Poco:enable_crypto=True", \
        "Poco:enable_data=False", \
        "Poco:enable_data_sqlite=False", \
        "Poco:enable_data_mysql=False", \
        "Poco:enable_data_odbc=False", \
        "Poco:enable_sevenzip=False", \
        "Poco:enable_zip=False", \
        "Poco:enable_apacheconnector=False", \
        "Poco:enable_cppparser=False", \
        "Poco:enable_pocodoc=False", \
        "Poco:enable_pagecompiler=False", \
        "Poco:enable_pagecompiler_file2page=False", \
        "cpprestsdk:shared=False", \
        "aws-sdk-cpp:shared=False", \
        "aws-sdk-cpp:build_s3=True", \
        "libharu:shared=False"
    generators = "cmake"

