# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerRegistryArtifactEventTarget(Model):
    """The target of the event.

    :param media_type: The MIME type of the artifact.
    :type media_type: str
    :param size: The size in bytes of the artifact.
    :type size: long
    :param digest: The digest of the artifact.
    :type digest: str
    :param repository: The repository name of the artifact.
    :type repository: str
    :param tag: The tag of the artifact.
    :type tag: str
    :param name: The name of the artifact.
    :type name: str
    :param version: The version of the artifact.
    :type version: str
    """

    _attribute_map = {
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'digest': {'key': 'digest', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, *, media_type: str=None, size: int=None, digest: str=None, repository: str=None, tag: str=None, name: str=None, version: str=None, **kwargs) -> None:
        super(ContainerRegistryArtifactEventTarget, self).__init__(**kwargs)
        self.media_type = media_type
        self.size = size
        self.digest = digest
        self.repository = repository
        self.tag = tag
        self.name = name
        self.version = version
