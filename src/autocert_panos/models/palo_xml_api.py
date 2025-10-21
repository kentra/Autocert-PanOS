from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict


class SubjectHash(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class IssuerHash(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class NotValidBefore(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class Issuer(BaseModel):
    admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class NotValidAfter(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class CommonName(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class ExpiryEpoch(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class Ca(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class Subject(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class PublicKey(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    text: str = Field(..., alias="#text")


class Algorithm(BaseModel):
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    # text: str = Field(..., alias="#text")
    model_config = SettingsConfigDict(extra="ignore")


class Entry(BaseModel):
    name: str = Field(..., alias="@name")
    # admin: str = Field(..., alias="@admin")
    # dirtyId: str = Field(..., alias="@dirtyId")
    # time: str = Field(..., alias="@time")
    subject_hash: SubjectHash = Field(..., alias="subject-hash")
    issuer_hash: IssuerHash = Field(..., alias="issuer-hash")
    not_valid_before: NotValidBefore = Field(..., alias="not-valid-before")
    issuer: Issuer
    not_valid_after: NotValidAfter = Field(..., alias="not-valid-after")
    commonname: CommonName = Field(..., alias="common-name")
    expiry_epoch: ExpiryEpoch = Field(..., alias="expiry-epoch")
    ca: Ca
    subject: Subject
    # public_key: PublicKey = Field(..., alias="public-key")
    algorithm: Algorithm
    # private_key: str = Field(..., alias="private-key")
    commonname_int: str = Field(..., alias="common-name-int")
    subject_int: str = Field(..., alias="subject-int")
    model_config = SettingsConfigDict(extra="ignore")


class Result(BaseModel):
    # totalcount: str = Field(..., alias="@total-count")
    # count: str = Field(..., alias="@count")
    entry: Entry
    model_config = SettingsConfigDict(extra="ignore")


class Response(BaseModel):
    # status: str = Field(..., alias="@status")
    # code: str = Field(..., alias="@code")
    result: Result
    model_config = SettingsConfigDict(extra="ignore")


class Certficate(BaseModel):
    response: Optional[Response] = None
