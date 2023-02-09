# Copyright 2018-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import OrderedDict as OD

from evergreen_config_generator.variants import Variant


mobile_flags = (
    ' -DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY'
    ' -DCMAKE_FIND_ROOT_PATH_MODE_PACKAGE=ONLY'
    ' -DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER'
    ' -DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY'
)

# Returns minutes for batchtime.


def days(n):
    return n * 24 * 60


all_variants = [
    Variant('releng',
            '**Release Archive Creator',
            'ubuntu1804-test',
            ['make-release-archive',
             'release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile .stdflags',
             '.debug-compile !.sspi .openssl !.asan-clang',
             OD([('name', 'debug-compile-sasl-openssl-static'),
                 ('distros', ['ubuntu1804-build'])]),
             OD([('name', 'debug-compile-nosasl-openssl-static'),
                 ('distros', ['ubuntu1804-build'])]),
             '.debug-compile !.sspi .nossl',
             'debug-compile-no-counters',
             'compile-tracing',
             'link-with-cmake',
             'link-with-cmake-deprecated',
             'abi-compliance-check',
             'link-with-cmake-ssl',
             'link-with-cmake-ssl-deprecated',
             'link-with-cmake-snappy',
             'link-with-cmake-snappy-deprecated',
             OD([('name', 'link-with-cmake-mac'), ('distros', ['macos-1014'])]),
             OD([('name', 'link-with-cmake-mac-deprecated'),
                 ('distros', ['macos-1014'])]),
             OD([('name', 'link-with-cmake-windows'),
                 ('distros', ['windows-64-vs2017-test'])]),
             OD([('name', 'link-with-cmake-windows-ssl'),
                 ('distros', ['windows-64-vs2017-test'])]),
             OD([('name', 'link-with-cmake-windows-snappy'),
                 ('distros', ['windows-64-vs2017-test'])]),
             OD([('name', 'link-with-cmake-mingw'),
                 ('distros', ['windows-64-vs2017-test'])]),
             OD([('name', 'link-with-pkg-config'),
                 ('distros', ['ubuntu1804-test'])]),
             OD([('name', 'link-with-pkg-config-mac'),
                 ('distros', ['macos-1014'])]),
             'link-with-pkg-config-ssl',
             'link-with-bson',
             OD([('name', 'link-with-bson-windows'),
                 ('distros', ['windows-64-vs2017-test'])]),
             OD([('name', 'link-with-bson-mac'), ('distros', ['macos-1014'])]),
             OD([('name', 'link-with-bson-mingw'),
                 ('distros', ['windows-64-vs2013-compile'])]),
             'check-headers',
             'install-uninstall-check',
             OD([('name', 'install-uninstall-check-mingw'),
                 ('distros', ['windows-64-vs2017-test'])]),
             OD([('name', 'install-uninstall-check-msvc'),
                 ('distros', ['windows-64-vs2017-test'])]),
             'debug-compile-with-warnings',
             OD([('name', 'build-and-test-with-toolchain'),
                 ('distros', ['debian10-small'])])],
            {}),
    Variant('clang34ubuntu',
            'clang 3.4 (Ubuntu 14.04)',
            'ubuntu1404-build',
            ['debug-compile-scan-build',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-rdtscp',
             '.debug-compile !.sspi .openssl !.client-side-encryption',
             '.debug-compile !.sspi .nossl',
             '.4.0 .openssl !.nosasl .server',
             '.3.6 .openssl !.nosasl .server'],
            {'CC': 'clang'}),
    Variant('clang35',
            'clang 3.5 (Debian 8.1)',
            'debian81-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile .stdflags',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.4.0 .openssl !.nosasl .server'],
            {'CC': 'clang'}),
    Variant('clang38',
            'clang 3.8 (Debian 9.2)',
            'debian92-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile .stdflags',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .openssl-static',
             '.debug-compile !.sspi .nossl',
             '.latest .openssl !.nosasl .server',
             '.latest .openssl-static !.nosasl .server',
             '.latest .nossl',
             '.5.0 .openssl !.nosasl .server',
             '.4.4 .openssl !.nosasl .server',
             '.4.2 .openssl !.nosasl .server'],
            {'CC': 'clang'}),
    Variant('openssl',
            'OpenSSL / LibreSSL',
            'archlinux-build',
            ['build-and-run-authentication-tests-openssl-1.0.1',
             'build-and-run-authentication-tests-openssl-1.0.2',
             'build-and-run-authentication-tests-openssl-1.1.0',
             'build-and-run-authentication-tests-openssl-1.0.1-fips',
             'build-and-run-authentication-tests-libressl-2.5',
             'build-and-run-authentication-tests-libressl-3.0-auto',
             'build-and-run-authentication-tests-libressl-3.0'],
            {}),
    Variant('clang37',
            'clang 3.7 (Archlinux)',
            'archlinux-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile .stdflags',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.4.0 .nossl',
             '.3.6 .nossl'],
            {'CC': 'clang'}),
    Variant('clang60-i686',
            'clang 6.0 (i686) (Ubuntu 18.04)',
            'ubuntu1804-test',
            ['debug-compile-scan-build',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile .stdflags',
             '.debug-compile !.sspi .nossl .nosasl',
             '.latest .nossl .nosasl',
             '.5.0 .nossl .nosasl',
             '.4.4 .nossl .nosasl',
             '.4.2 .nossl .nosasl',
             '.4.0 .nossl .nosasl'],
            {'CC': 'clang', 'MARCH': 'i686'}),
    Variant('clang38-i686',
            'clang 3.8 (i686) (Ubuntu 16.04)',
            'ubuntu1604-test',
            ['debug-compile-scan-build',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile .stdflags',
             '.debug-compile !.sspi .nossl .nosasl',
             '.3.6 .nossl .nosasl'],
            {'CC': 'clang', 'MARCH': 'i686'}),
    Variant('clang38ubuntu',
            'clang 3.8 (Ubuntu 16.04)',
            'ubuntu1604-test',
            ['.compression !.zstd',
             'debug-compile-scan-build',
             'debug-compile-asan-clang',
             'debug-compile-ubsan',
             'debug-compile-ubsan-with-extra-alignment',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile .stdflags',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.4.4 .openssl !.nosasl .server',
             '.4.2 .openssl !.nosasl .server',
             '.4.0 .openssl !.nosasl .server',
             '.3.6 .openssl !.nosasl .server'],
            {'CC': 'clang'}),
    Variant('gcc48ubuntu',
            'GCC 4.8 (Ubuntu 14.04)',
            'ubuntu1404-build',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.4.0 .openssl !.nosasl .server',
             '.3.6 .openssl !.nosasl .server'],
            {'CC': 'gcc'}),
    Variant('gcc82rhel',
            'GCC 8.2 (RHEL 8.0)',
            'rhel80-test',
            ['.hardened',
             '.compression !.snappy !.zstd',
             'release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.latest .openssl !.nosasl .server',
             '.latest .nossl'],
            {'CC': 'gcc'}),
    Variant('gcc48rhel',
            'GCC 4.8 (RHEL 7.0)',
            'rhel70',
            # Skip client-side-encryption tests on RHEL 7.0 due to OCSP errors
            # with Azure. See CDRIVER-3620 and CDRIVER-3814.
            ['.hardened',
             '.compression !.snappy',
             'release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl !.client-side-encryption',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.latest .openssl !.nosasl .server !.client-side-encryption',
             '.latest .nossl',
             '.5.0 .openssl !.nosasl .server !.client-side-encryption',
             '.4.4 .openssl !.nosasl .server !.client-side-encryption',
             '.4.2 .openssl !.nosasl .server !.client-side-encryption',
             '.4.0 .openssl !.nosasl .server !.client-side-encryption',
             '.3.6 .openssl !.nosasl .server !.client-side-encryption'],
            {'CC': 'gcc'}),
    Variant('gcc49',
            'GCC 4.9 (Debian 8.1)',
            'debian81-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.4.0 .openssl !.nosasl .server'],
            {'CC': 'gcc'}),
    Variant('gcc63',
            'GCC 6.3 (Debian 9.2)',
            'debian92-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .openssl-static',
             '.debug-compile !.sspi .nossl',
             '.latest .openssl !.nosasl .server',
             '.latest .openssl-static !.nosasl .server',
             '.latest .nossl',
             '.5.0 .openssl !.nosasl .server',
             '.4.4 .openssl !.nosasl .server',
             '.4.2 .openssl !.nosasl .server'],
            {'CC': 'gcc'}),
    Variant('gcc83',
            'GCC 8.3 (Debian 10.0)',
            'debian10-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .openssl-static',
             '.debug-compile !.sspi .nossl',
             '.latest .openssl !.nosasl .server',
             '.latest .openssl-static !.nosasl .server',
             '.latest .nossl'],
            {'CC': 'gcc'}),
    Variant('gcc102',
            'GCC 10.2 (Debian 11.0)',
            'debian11-large',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .openssl-static',
             '.debug-compile !.sspi .nossl',
             '.latest .openssl !.nosasl .server',
             '.latest .openssl-static !.nosasl .server',
             '.latest .nossl'],
            {'CC': 'gcc'}),
    Variant('gcc94',
            'GCC 9.4 (Ubuntu 20.04)',
            'ubuntu2004-large',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .openssl-static',
             '.debug-compile !.sspi .nossl',
             '.latest .openssl !.nosasl .server',
             '.latest .openssl-static !.nosasl .server',
             '.latest .nossl'],
            {'CC': 'gcc'}),
    Variant('gcc75-i686',
            'GCC 7.5 (i686) (Ubuntu 18.04)',
            'ubuntu1804-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile !.sspi .nossl .nosasl',
             '.latest .nossl .nosasl',
             '.5.0 .nossl .nosasl',
             '.4.4 .nossl .nosasl',
             '.4.2 .nossl .nosasl',
             '.4.0 .nossl .nosasl'],
            {'CC': 'gcc', 'MARCH': 'i686'}),
    Variant('gcc75',
            'GCC 7.5 (Ubuntu 18.04)',
            'ubuntu1804-test',
            ['.compression !.zstd',
             'debug-compile-asan-gcc',
             'debug-compile-nosrv',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.authentication-tests .asan',
             '.test-coverage',
             '.latest .openssl !.nosasl .server',
             '.latest .nossl',
             '.latest .openssl .nosasl .replica_set',
             '.latest .openssl !.nosasl .replica_set',
             'retry-true-latest-server',
             '.5.0 .openssl !.nosasl .server',
             '.4.4 .openssl !.nosasl .server',
             '.4.2 .openssl !.nosasl .server',
             '.4.0 .openssl !.nosasl .server',
             '.4.0 .openssl !.nosasl .replica_set',
             'test-dns-openssl',
             'test-dns-auth-openssl',
             'test-dns-loadbalanced-openssl'
             ],
            {'CC': 'gcc'}),
    Variant('gcc54',
            'GCC 5.4 (Ubuntu 16.04)',
            'ubuntu1604-test',
            ['.compression !.zstd',
             'debug-compile-asan-gcc',
             'debug-compile-nosrv',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             ],
            {'CC': 'gcc'}),
    Variant('darwin',
            '*Darwin, macOS (Apple LLVM)',
            'macos-1014',
            ['.compression !.snappy !.zstd',
             # Remove !.zstd in CDRIVER-3483.
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-rdtscp',
             'debug-compile-no-align',
             'debug-compile-nosrv',
             '.debug-compile .darwinssl',
             '.debug-compile !.sspi .nossl',
             '.debug-compile .clang',
             '.authentication-tests .darwinssl',
             '.latest .darwinssl !.nosasl .server',
             '.latest .nossl',
             '.5.0 .darwinssl !.nosasl .server',
             '.4.4 .darwinssl !.nosasl .server',
             '.4.2 .darwinssl !.nosasl .server',
             '.4.0 .darwinssl !.nosasl .server',
             '.3.6 .darwinssl !.nosasl .server',
             'test-dns-darwinssl',
             'test-dns-auth-darwinssl',
             'debug-compile-lto',
             'debug-compile-lto-thin',
             'debug-compile-aws',
             'test-aws-openssl-regular-4.4',
             'test-aws-openssl-regular-latest'
             ],
            {'CC': 'clang'}),
    Variant('windows-2017-32',
            'Windows (i686) (VS 2017)',
            'windows-64-vs2017-test',
            ['.debug-compile .winssl .nosasl',
             '.debug-compile !.sspi .nossl .nosasl',
             '.debug-compile .sspi !.openssl !.openssl-static',
             '.server .winssl .latest .nosasl',
             '.latest .nossl .nosasl',
             '.nosasl .latest .nossl',
             '.sspi .latest',
             ],
            {'CC': 'Visual Studio 15 2017'}),
    Variant('windows-2017',
            'Windows (VS 2017)',
            'windows-64-vs2017-test',
            ['.debug-compile .winssl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.debug-compile .sspi !.openssl-static',
             '.server .winssl .latest',
             '.server .openssl .latest !.nosasl',
             '.latest .nossl',
             '.nosasl .latest .nossl',
             '.sspi .latest',
             'test-dns-winssl',
             'test-dns-auth-winssl',
             'debug-compile-aws',
             '.5.0 .winssl !.nosasl .server',
             '.4.4 .winssl !.nosasl .server',
             'test-aws-openssl-regular-4.4',
             'test-aws-openssl-regular-latest',
             # Authentication tests with OpenSSL on Windows are only run on the vs2017 variant.
             # Older vs variants fail to verify certificates against Atlas tests.
             '.authentication-tests .openssl !.sasl',
             '.authentication-tests .winssl'
             ],
            {'CC': 'Visual Studio 15 2017 Win64'}),
    Variant('windows-2015',
            'Windows (VS 2015)',
            'windows-64-vs2015-compile',
            ['.compression !.snappy !.zstd !.latest',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             'debug-compile-nosrv',
             '.debug-compile .winssl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.debug-compile .sspi !.openssl-static',
             '.authentication-tests .winssl',
             '.4.2 .winssl !.nosasl .server',
             '.4.0 .winssl !.nosasl .server',
             '.3.6 .winssl !.nosasl .server'],
            {'CC': 'Visual Studio 14 2015 Win64'}),
    Variant('windows-2015-32',
            'Windows (i686) (VS 2015)',
            'windows-64-vs2015-compile',
            ['.compression !.snappy !.zstd !.latest',
             'release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile .sspi !.openssl !.openssl-static',
             '.debug-compile .winssl .nosasl',
             '.debug-compile !.sspi .nossl .nosasl',
             '.authentication-tests .winssl',
             '.4.2 .winssl .nosasl .server',
             '.4.0 .winssl .nosasl .server'],
            {'CC': 'Visual Studio 14 2015'}),
    Variant('windows-2013',
            'Windows (VS 2013)',
            'windows-64-vs2013-compile',
            ['.compression !.snappy !.zstd !.latest',
             'release-compile',
             'debug-compile-nosasl-nossl',
             # libmongocrypt does not compile on pre-VS2015. Prohibit CSE.
             '.debug-compile .winssl !.client-side-encryption',
             '.debug-compile !.sspi .openssl !.client-side-encryption',
             '.debug-compile !.sspi .nossl',
             '.debug-compile .sspi !.client-side-encryption !.openssl-static',
             '.authentication-tests .winssl',
             '.4.2 .winssl !.nosasl .server !.client-side-encryption',
             '.4.0 .winssl !.nosasl .server'],
            {'CC': 'Visual Studio 12 2013 Win64'}),
    Variant('windows-2013-32',
            'Windows (i686) (VS 2013)',
            'windows-64-vs2013-compile',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             'debug-compile-rdtscp',
             '.debug-compile .sspi !.openssl !.openssl-static',
             '.debug-compile .winssl .nosasl !.client-side-encryption',
             '.debug-compile !.sspi .nossl .nosasl',
             '.authentication-tests .winssl',
             '.4.2 .winssl .nosasl .server !.client-side-encryption',
             '.4.0 .winssl .nosasl .server'],
            {'CC': 'Visual Studio 12 2013'}),
    Variant('mingw-windows2016',
            'MinGW-W64 (Windows Server 2016)',
            'windows-64-vs2017-test',
            ['debug-compile-nosasl-nossl',
             '.debug-compile .winssl .sspi',
             '.latest .nossl .nosasl .server',
             '.latest .winssl .sspi .server'],
            {'CC': 'mingw'}),
    Variant('mingw',
            'MinGW-W64',
            'windows-64-vs2013-compile',
            ['debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile .nossl .nosasl',
             '.debug-compile .winssl .sspi'],
            {'CC': 'mingw'}),
    Variant('power8-rhel81',
            'Power8 (ppc64le) (RHEL 8.1)',
            'rhel81-power8-test',
            ['release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl !.client-side-encryption',
             '.debug-compile !.sspi .nossl',
             '.latest .openssl !.nosasl .server !.client-side-encryption',
             '.latest .nossl',
             '.5.0 .openssl !.nosasl .server !.client-side-encryption',
             '.4.4 .openssl !.nosasl .server !.client-side-encryption',
             '.4.2 .openssl !.nosasl .server !.client-side-encryption',
             'test-dns-openssl'],
            {'CC': 'gcc'},
            batchtime=days(1)),
    Variant('arm-ubuntu1804',
            '*ARM (aarch64) (Ubuntu 18.04)',
            'ubuntu1804-arm64-large',
            ['.compression !.snappy !.zstd',
             'debug-compile-scan-build',
             'debug-compile-no-align',
             'release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.latest .openssl !.nosasl .server',
             '.latest .nossl',
             '.5.0 .openssl !.nosasl .server',
             '.4.4 .openssl !.nosasl .server',
             '.4.2 .openssl !.nosasl .server',
             'test-dns-openssl'],
            {'CC': 'gcc'},
            batchtime=days(1)),
    Variant('arm-ubuntu1604',
            '*ARM (aarch64) (Ubuntu 16.04)',
            'ubuntu1604-arm64-large',
            ['.compression !.snappy !.zstd',
             'debug-compile-scan-build',
             'debug-compile-no-align',
             'release-compile',
             'debug-compile-nosasl-nossl',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.4.0 .openssl !.nosasl .server'],
            {'CC': 'gcc'},
            batchtime=days(1)),
    Variant('zseries-rhel83',
            '*zSeries',
            'rhel83-zseries-small',
            ['release-compile',
             #      '.compression', --> TODO: waiting on ticket CDRIVER-3258
             'debug-compile-nosasl-nossl',
             'debug-compile-no-align',
             '.debug-compile !.sspi .openssl',
             '.debug-compile !.sspi .nossl',
             '.authentication-tests .openssl',
             '.latest .openssl !.nosasl .server',
             '.latest .nossl',
             '.6.0 .openssl !.nosasl .server',
             '.5.0 .openssl !.nosasl .server'],
            {'CC': 'gcc'},
            batchtime=days(1)),
    Variant('asan-ubuntu',
            'ASAN Tests (Ubuntu 18.04)',
            'ubuntu1804-test',
            ['.debug-compile .asan-clang',
             '.test-asan !.3.6'],
            {'CC': 'clang'},
            batchtime=days(1)),
    Variant('asan-ubuntu-with-mongocryptd',
            'ASAN Tests with mongocryptd (Ubuntu 18.04)',
            'ubuntu1804-test',
            ['debug-compile-asan-openssl-cse',
             '.test-asan !.3.6 .client-side-encryption'],
            {'CC': 'clang', 'SKIP_CRYPT_SHARED_LIB': 'on'},
            batchtime=days(1)),
    # There is no MongoDB < 4.0 with SSL available on Ubuntu post 16.04.
    # So have a variant for ASAN to test against MongoDB 3.6.
    Variant('asan-ubuntu-ubuntu1604',
            'ASAN Tests (Ubuntu 16.04)',
            'ubuntu1604-test',
            ['.debug-compile .asan-clang',
             '.test-asan .3.6'],
            {'CC': 'clang'},
            batchtime=days(1)),
    Variant('clang60ubuntu', 'clang 6.0 (Ubuntu 18.04)', 'ubuntu1804-test', [
        'debug-compile-aws',
        'debug-compile-nosasl-openssl-static',
        'debug-compile-sasl-openssl-static',
        'debug-compile-sspi-openssl-static',
        '.authentication-tests .asan',
        'test-aws-openssl-regular-latest',
        'test-aws-openssl-ec2-latest',
        'test-aws-openssl-ecs-latest',
        'test-aws-openssl-assume_role-latest',
        'test-aws-openssl-lambda-latest',
        'test-aws-openssl-regular-4.4',
        'test-aws-openssl-ec2-4.4',
        'test-aws-openssl-ecs-4.4',
        'test-aws-openssl-assume_role-4.4',
        'test-aws-openssl-lambda-4.4'
    ], {'CC': 'clang'}),
    Variant('mongohouse',
            'Mongohouse Test',
            'ubuntu1804-test',
            ['debug-compile-sasl-openssl',
             'test-mongohouse'],
            {}),
    Variant('ocsp', 'OCSP tests', 'ubuntu2004-small', [
        OD([('name', 'debug-compile-nosasl-openssl')]),
        OD([('name', 'debug-compile-nosasl-openssl-static')]),
        OD([('name', 'debug-compile-nosasl-darwinssl'), ('distros', ['macos-1014'])]),
        OD([('name', 'debug-compile-nosasl-winssl'),
           ('distros', ['windows-64-vs2017-test'])]),
        OD([('name', '.ocsp-openssl')]),
        OD([('name', '.ocsp-darwinssl'), ('distros', ['macos-1014'])]),
        OD([('name', '.ocsp-winssl'), ('distros', ['windows-64-vs2017-test'])]),
        OD([('name', 'debug-compile-nosasl-openssl-1.0.1')]),
        OD([('name', '.ocsp-openssl-1.0.1')])
    ], {}, batchtime=days(7)),
    Variant('packaging', 'Linux Distro Packaging', 'ubuntu1804-test', [
        'debian-package-build',
        OD([('name', 'rpm-package-build'), ('distros', ['rhel82-arm64-small'])]),
    ], {}, batchtime=days(1)),
    Variant('tsan-ubuntu',
            'Thread Sanitizer (TSAN) Tests (Ubuntu 18.04)',
            'ubuntu1804-small',
            ['.tsan !.3.6'],
            {'CC': '/opt/mongodbtoolchain/v3/bin/clang'},
            batchtime=days(1)),
    Variant('versioned-api',
            'Versioned API Tests',
            'ubuntu1804-test',
            ['debug-compile-nosasl-openssl',
             'debug-compile-nosasl-nossl',
             '.versioned-api'],
            {}),
    Variant('macos_m1',
            'macOS m1 (Apple LLVM)',
            'macos-1100-arm64',
            ['debug-compile-sasl-darwinssl'],
            {'CC': 'clang'}),
]
