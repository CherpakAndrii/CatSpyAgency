from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from database.sqlite_connector import engine, Session


Base = declarative_base()


class SpyCat(Base):
    __tablename__ = "cats"

    cat_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    experience = Column(Integer, nullable=False)
    breed = Column(String(20), nullable=False)
    salary = Column(Integer, nullable=False)

    missions = relationship('Mission', back_populates='spy_cat')

    def to_dict(self):
        return {
            'cat_id': self.cat_id,
            'name': self.name,
            'experience': self.experience,
            'breed': self.breed,
            'salary': self.salary
        }

    def to_extended_dict(self):
        return {
            'cat_id': self.cat_id,
            'name': self.name,
            'experience': self.experience,
            'breed': self.breed,
            'salary': self.salary,
            'missions': [mission.to_dict() for mission in self.missions]
        }


class MissionTarget(Base):
    __tablename__ = "targets"

    target_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    country = Column(String(30), nullable=False)
    is_complete = Column(Integer, nullable=False, default=0)

    mission_id = Column(Integer, ForeignKey('missions.mission_id', ondelete='CASCADE'))

    notes = relationship('TargetNote', back_populates='target')
    mission = relationship('Mission', back_populates='targets')

    def to_extended_dict(self):
        return {
            'target_id': self.target_id,
            'name': self.name,
            'country': self.country,
            'is_complete': self.is_complete,
            'notes': [note.to_dict() for note in self.notes]
        }


class TargetNote(Base):
    __tablename__ = "notes"

    note_id = Column(Integer, primary_key=True)
    text = Column(String(500), nullable=False)

    target_id = Column(Integer, ForeignKey('targets.target_id', ondelete='CASCADE'))

    target = relationship('MissionTarget', back_populates='notes')

    def to_dict(self):
        return {
            'note_id': self.note_id,
            'text': self.text
        }


class Mission(Base):
    __tablename__ = "missions"

    mission_id = Column(Integer, primary_key=True)
    cat_id = Column(Integer, ForeignKey('cats.cat_id', ondelete='CASCADE'), nullable=True)
    is_complete = Column(Integer, nullable=False, default=0)

    spy_cat = relationship('SpyCat', back_populates='missions')
    targets = relationship('MissionTarget', back_populates='mission')

    def to_dict(self):
        return {
            'mission_id': self.mission_id,
            'cat_id': self.cat_id,
            'is_complete': self.is_complete
        }

    def to_extended_dict(self):
        return {
            'mission_id': self.mission_id,
            'cat_id': self.cat_id,
            'is_complete': self.is_complete,
            'spy_cat': self.spy_cat.to_dict() if self.spy_cat else None,
            'targets': [target.to_extended_dict() for target in self.targets]
        }


Base.metadata.create_all(engine)
