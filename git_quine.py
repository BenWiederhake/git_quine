#!/usr/bin/env python3

import json
import lzma
import os
import shutil
import subprocess


EXECUTABLES = ['git_quine.py', 'quine_helper.py']
REPOSITORY = 'fd377a585a000004e6d6b4460200210116000000742fe5a3e01c220c0d5d002de084623809446e99f3a540dbb4c7646e3fb1fad2e303b26d70f9ac6013ad9cc535a04d25e4205a74bfcc29c757b0ec1a05675f997a8c2e052565018a770e24057a331aadd218c1cd5c3650715b47245ba0d346c87a6f03dee71565a7c03a5f4f3a4b7d42852160164fbdd41d7dd6548df1510fddf2c2f11086ff6a665fb480c0ec0a165fd5aefcdc5b1f313adb0d8eb59348d6b3014cece3f10d22daa67e5f122d419cb1c10a4203e36a1979d872f9a78ee689a91268bf3e9cfcc68099c8ce0ae78e1b27f6e376e912cf3f2d48082cba2da97cce9ac21360a0592e6c25ff8e6dbe682d4da5a451b53f54a68afe0bbab317101e0bec76b039b78741407b698b242260c239b78e8283ba4d8d3fb535d8c51ca0caebdbd8e12aae4e055c3ebec90ec74e91956e963fb3ceba45f17a3efb068d4c8859967cb86b0e374d84fe405935b78dd65afea1999e5f45e8c10823db5d2dce8e8a53a3109049f96b88e974df899547e4dbf6a0efed6f49d9d9ebd615e9002db9f21efbd20f5680d9e72ff22b9f9fa96573165e94975493bf4ae9ca80ecb5843d313ec13b043fad6463b6a6a64be9a5a722807dbf2acc2dc424f28f6b67513f6cb3f60e8d3165898dd187e391440ec1d34f8f67a82d19fe07de14f8f8bfdb954e441c3785d935200e675cf7eefb21685913afa02257678ddc9425b9abcc259621457328197154c0f6cd71edb7a182cac28157cd7d70260a09ff0dde75f28b8901fca9b0a401f5b9ddf2ce681d28e961f665f74579575103ef02ce800359319ed169021a1ab047c91d35b2c988a1ef9a5ca692620d251f3752d5b79a3dfa6a9ae4c20f6984bdbb62b46855201c60b9c89f740ba2a0c9eb57e30306903dfbfe6dff42eb53cb805c8a0b8918542982dd68ac4d18b0f87a672e5c58c994666257df51c5c0e1b68494c8b74a6e2a66195b763b22d2e6e846c2c0ec9a35c2c565e00dc5d199ac6b42b4625ac72b7acbcbda89501c5c31198a5b00ebedb20e7af9c419c042954faf4e3981b0677a3f7977a306749f67fcb28f1f2e1c239eee1a34239bebd1db0b69d24ff1aef2eb543f257d7e8dc61f67cca0ccd267aa661277c2ad8d9ab1653621bf15d96961139045847e568c1e250084c7ddeb2febd8a1c7f308dae32704b4b46a541deb6249dcceba19024d78357cbd7554f5ee7ffe4258e96ef9c401e66265c1edb2fcc637394341b2e6b2b2447917bf408d88542ff628f268f78f0d1cd3cc6dabfe400d845cb2a9c785801edebe7b13de263ddec31640a2e4ff61fa1e171c347215d3b5dacc389a5222f6e1a16756f45cdfa8b53fb6d60a703ff203dff23a6a2a8729e72c3b92bf84e16b56c8c0eb72885449075e3f6112aa568dc084a96a4b06062bf40c7ddd0da3f2ba4079f1af771aa018d973f433da026efe372aa0a73ee5cdcc77a644000d5cae3581515df9b8d03473372f158379832381031d5ced653937c215bb58c7b90bd460b2db2c6f3b6685b77da497f50400d73d8107ef92442264661013bf88bf07e29905a65469d16597b4a4a50cb269d4c672d1575f447099f83298736e5443a52ec5c07a13f33351be877f53496aaa1dc810d026f412c28cc8f4b02b211a346313750c21728bdf7676e2eb356de8927267801e2ce48521e4ea603309edb74365e98a700ba2149743271477bc2f574b381321bab9a8ab167b55a347ec8c14dd7e2efbb9df894be9778fd7d44316cc3b497c5ec75993e33418d0442e1fa6c1794d5bff1bfa9199aeaf482dae2f4177b4a7b80e9e7f238d36ddebbbcc6bfa231965a69570fe174c01b0086c86749a5c7bb43925a1981fda266f734adac66bc7bb177b3013b97f27c59720ab32eaf5b24a33017bf250d95506cde2378dced0da0968dcca88e90f95417b2b75c30a5316d6c9bd5b482a5462e031ee173d0583e6d5f45d57d4a25900e0326943e4882feca3192d64bd83e02e2bb13898104fac9a14f7341e6a5a949418ae8a2ba8f12aa9c9c9565fce9f457bb06e41f6f11f154d4cceb393f1d510ea0872ef9e6e60388501584b3f41df565510047b6b4e6d5a34b6fbeb6d2b8b41964781dbe3c662e51756ff0354bbaef9eb9cabdeb541d5969714cacc997809591ff0eba977214f025c5e670ea025300dc3cc62e9d90d4c76da6ba27ac790d07a25e0e656b12921b68f496e6b2ccaf08c6112d377cd0ab11e1d21ef18d0750bb5894518704dbfe9fb242ba3049b32d28926643751d02b84d496ef921e3758b87a832417915543f5b981ccccb933f4aa4bef3122e9a03695cb0d543a96a7b2fc30e4f92495c41b2f6ae024ed9b0035c769773d0b9901c82769aadc92ab451421107747b92df1a9f53c9996d39340c89143973aac80d6089c2a8d951a2daa9f85dc556aaa1264c6abcb7ef9145a0b57a9d8e1a769edf9915345bd711b9b40abc252916a52982f274c30aac7edd47adba2d35e8761c5719c67ee3b89c39cddf35534cbc8704f740715aa83e00fa7551a1007ba3f05c2fb802cc36ce98fe9305607c723b07edee68b13a088a3dca921ee24cf618ba59c675ea29cbd4ce531e83e132f5f0e6eeba3ff2b338f444cca8d60adb3322a9c227ed1176d6297a971d9d2f3c839603f1601f5876251b6ad69e271c1e2bb66a36a277785d550ffff97dac50290731509bb6417266c2b9acae5004e513d3483663009c139580c6d7948a684ac3761b0620312ac916ba2fb19fd09649d1339a00f44a1384d4be609ee573a532054d0101beee9e206325f18486d75c565eda5bdc5679b7360251000b7ad0cef4a405678e1e263a4ce70240244e8696f1fa7afecff5cfcc333bfca9260064917ae8e4ba82f7dea0d74d7334f31134394e59d1132c13867818c6ee91afd9fce71b20852a82fb0737d6e97fe82c2535b3c8191d703228598c68fe0c99463218cb0648d5b3a757aca59897df6e1d3f25714741574a757a067864b281a14a838a97972a4e940d583ca9c6420bb984ec6f9206b5871005564e87286b21369c9a28368f7387458541cabaf0f7656796627c3c2f392414b1052bd49819fbf70ca0fc569228fd591ff54b8ad3f97d6438de74c126440fb43ffb6581624eccf452126dcb4dbdeb5d463bacbf28f0efcf2ee4860d00842d2d1caed08e58600db8fb700cbcd704c5edab798f419730957885e0766ff5f4ba1e73752822e0e133312cee1cc123a1943a6ebf4eeef2c21e71650a4e687494b7dbf9269446a4a45771d1a156eab7bba1ec9f8995eaf8f201aa98df1e9d814c5345f98b2de7a796951f21e99d3693b5e24bf282c6106c6ff0b80969f941b1bd60de04d40086b05a70a1db09f4f78d3beef019301b989815cd79dd3b9d1bfaead7e821302b94650625190374de0ecab97d909825680e9e3f67244a83b49a131e6e7cc3929ee2fba3241f1ea5cf48c0177c12d1a1b51ea29d8cc3c37d02e1d771e0c5bf8372fed612e758ede267927a4e3a103cb351066d4d51a9b948200be3610f701839047a36b967a1226bbc927b581a688bfd91dafa515de6328fa86da64e344cb2733a89c0bea7a7c6a633f87d3a8de193d1cdf71463dcfa55dc46c62b618c2cff259ff396c8a242d9e6a46f6db2ae0fde31cc786bda945c89972e9e2c2196748714acc15c7af1979dda6febca51b715e7ed9ded23a32180ed0ebfadaa8ba8c2268a381c2586e7679bef2bafcfeb2bf8053b9f7feb12f483459a2df527a18aefa0287e32194a96f5ba25930bdf156bab6452d2afd906649baaaa7bf543d7fbaef0a36e48fb584e114a31d708a3ff47a1ef83589620e07b2780001746832f277707b084ec0304f20bccd6c2091f1df2f6f66cbee78e3ae3e2299b39cfa0cfa0e0a229f86f9ce82ecf33728328ce97c9783e1e54a8403a06c73f66f58b535bf14622ed42f42ced06b5926b0ae0797bb8020be2ff530e403e8cf8eabef86a887f7184096a7cfee01a3015d1e24c0b4d72a1f7b1031c921cdb769787a43d2449caccd4510862fc689d661fd8be9a9d34711238aad2072a2df661e08b65431470e00f3252ca2d79279c8ae747ae35cc0a6c1d4b5d4396966051879490a123e76dc9747118d979adbbfe17e98e02653e098ccb4c9567d68bff355ed2191050f59692a123786048c373aedc7310526339f5955422a5940cee510a0b5b331fac8d82509b222e8f17c55832bb463063c252fce96729311b63dbb2c791db1e0091f95b490d4b62c322e72abcbbf109ba231bcd64aa24aaacf1334ba5fae8ba565fd1ea19db4be2be945f51e1dfcf7d507ad19acf80ffd9a27fb207cc27fac26b998e7ddd50b5935249a788b9708dca9108e6690502d85516f1100000000f69a3ab24356880c0001a918a33800007b4a70d8b1c467fb020000000004595a'

GIT_AUTHOR = [
    'GIT_COMMITTER_NAME=git_quine.py',
    'GIT_AUTHOR_NAME=git_quine.py',
    'GIT_COMMITTER_EMAIL=benwiederhake.github@gmx.de',
    'GIT_AUTHOR_EMAIL=benwiederhake.github@gmx.de',
]


def get_commits():
    return json.loads(lzma.decompress(bytes.fromhex(REPOSITORY)).decode('ascii'))


def wrap_commits(commits):
    json_commits = json.dumps(commits, separators=(',', ':'))
    return lzma.compress(json_commits.encode('ascii')).hex()


def call(*argv):
    subprocess.check_call(argv, stdout=subprocess.DEVNULL)


def run():
    if os.path.exists('git_quine'):
        shutil.rmtree('git_quine')
    os.mkdir('git_quine')
    os.chdir('git_quine')
    each_contents = get_commits()
    inited = False
    for i, commit in enumerate(each_contents):
        for name, content in commit[2]:
            if name == 'git_quine.py':
                previous_commits = wrap_commits(each_contents[:i + 1])
                content = content.format(previous_commits)
            with open(name, 'w') as f:
                f.write(content)
            if name in EXECUTABLES:
                os.chmod(name, 0o755)
            else:
                os.chmod(name, 0o644)
        if not inited:
            call('git', 'init')
            inited = True
        call('git', 'add', *[name for name, _ in commit[2]])
        commit_argv = ['env', 'GIT_COMMITTER_DATE=' + commit[0], 'GIT_AUTHOR_DATE=' + commit[0]]
        commit_argv.extend(GIT_AUTHOR)
        commit_argv.extend(['git', 'commit', '-m', commit[1], '--no-edit', '--no-gpg-sign', '--no-signoff'])
        call(*commit_argv)


if __name__ == '__main__':
    run()